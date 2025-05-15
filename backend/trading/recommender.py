from datetime import datetime, timedelta
import pandas as pd
import pytz
import os
import logging
from history.services import MT5Connector  # Assuming MT5Connector is in the same app
from .models import Stock, Currency, Commoditie, Index

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SignalRecommendationSystem:
    def __init__(self, account=None, password=None, server=None):
        """Initialize the recommendation system with MT5 credentials."""
        self.mt5_connector = MT5Connector(
            account=account ,
            password=password,
            server=server
        )
        self.timeframes = ['1wk', '1d', '4h']
        self.utc = pytz.UTC
        self.current_date = datetime.now(self.utc)

    def get_assets(self, asset_type=None):
        """Fetch assets from Django models, optionally filtered by asset type."""
        if asset_type == 'stock':
            return [(stock, 'stock') for stock in Stock.objects.all()]
        elif asset_type == 'currency':
            return [(currency, 'currency') for currency in Currency.objects.all()]
        elif asset_type == 'commodity':
            return [(commodity, 'commodity') for commodity in Commoditie.objects.all()]
        elif asset_type == 'index':
            return [(index, 'index') for index in Index.objects.all()]
        else:
            # Return all assets if no type is specified
            return [
                (stock, 'stock') for stock in Stock.objects.all()
            ] + [
                (currency, 'currency') for currency in Currency.objects.all()
            ] + [
                (commodity, 'commodity') for commodity in Commoditie.objects.all()
            ] + [
                (index, 'index') for index in Index.objects.all()
            ]

    def fetch_signals(self, symbol, asset_type):
        """Fetch signals for a given symbol and asset type across timeframes."""
        try:
            signals_df = self.mt5_connector.get_last_signal_by_timeframes(symbol, self.timeframes, asset_type)
            logger.info(f"Fetched signals for {symbol} ({asset_type}): {len(signals_df)} rows")
            return signals_df
        except Exception as e:
            logger.error(f"Failed to fetch signals for {symbol}: {str(e)}")
            return pd.DataFrame()

    def filter_recent_signals(self, signals_df):
        """Filter signals within the last 2 days."""
        if signals_df.empty:
            logger.info("No signals to filter.")
            return signals_df

        # Ensure two_days_ago is timezone-aware (UTC)
        two_days_ago = self.current_date - timedelta(days=1)
        
        # Ensure signals_df['time'] is timezone-aware (UTC)
        signals_df['time'] = pd.to_datetime(signals_df['time'], utc=True)
        
        # Log for debugging
        logger.debug(f"Type of signals_df['time']: {signals_df['time'].dtype}")
        logger.debug(f"Type of two_days_ago: {type(two_days_ago)}")
        logger.debug(f"Sample signal times: {signals_df['time'].head().tolist()}")
        logger.debug(f"Two days ago: {two_days_ago}")

        # Filter signals
        recent_signals = signals_df[signals_df['time'] >= two_days_ago]
        logger.info(f"Filtered {len(recent_signals)} recent signals within the last 2 days.")
        return recent_signals

    def generate_recommendations(self, asset_type=None):
        """Generate a DataFrame with recommendations based on recent signals for the specified asset type."""
        if not self.mt5_connector.initialize_mt5() or not self.mt5_connector.login():
            logger.error("Failed to connect to MT5.")
            return pd.DataFrame({"error": ["Failed to connect to MT5"]})

        assets = self.get_assets(asset_type)
        recommendations = []

        for asset, asset_type in assets:
            symbol = asset.symbol
            logger.info(f"Processing signals for {symbol} ({asset_type})")
            signals_df = self.fetch_signals(symbol, asset_type)
            recent_signals = self.filter_recent_signals(signals_df)

            if not recent_signals.empty:
                for _, row in recent_signals.iterrows():
                    recommendations.append({
                        'symbol': symbol,
                        'asset_type': asset_type,
                        'name': asset.name,
                        'timeframe': row['timeframe'],
                        'signal': row['signal'],
                        'signal_time': row['time'],
                        'price': row['price'],
                        'recommendation': 'Buy' if row['signal'] == 'buy' else 'Sell' if row['signal'] == 'sell' else 'None',
                        'img_url': asset.img.url if asset.img else None
                    })

        recommendations_df = pd.DataFrame(recommendations)
        if recommendations_df.empty:
            logger.info(f"No recent signals found for asset type {asset_type or 'all'}.")
            return pd.DataFrame({"message": [f"No recent signals within the last 2 days for {asset_type or 'all assets'}"]})

        # Sort by signal time (most recent first)
        recommendations_df.sort_values(by='signal_time', ascending=False, inplace=True)
        logger.info(f"Generated {len(recommendations_df)} recommendations for {asset_type or 'all assets'}.")
        return recommendations_df

    def shutdown(self):
        """Shutdown MT5 connection."""
        self.mt5_connector.shutdown()