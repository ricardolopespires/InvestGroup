import { useState } from 'react';
import { MdCurrencyExchange } from 'react-icons/md';
import { postInversorOperations } from '@/lib/actions/actions.operations';

// Define TypeScript interfaces for props
interface Operation {
  ticket: string;
  type: string;
}

interface InverterOperationsProps {
  operation: Operation;
}

const InverterOperations = ({ operation }: InverterOperationsProps) => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Retrieve user from localStorage
  const user = JSON.parse(localStorage.getItem('user') || '{}');

  const handleClick = async (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    setError(null);
    setIsLoading(true);

    if (!user?.email) {
      setError('User not found. Please log in.');
      setIsLoading(false);
      return;
    }

    if (!operation?.ticket || !operation?.type) {
      setError('Invalid operation data.');
      setIsLoading(false);
      return;
    }

    try {
      await postInversorOperations({ ticket: operation.ticket, UserId: user.email });
      // Optionally show success feedback (e.g., toast notification)
      console.log('Operation reversed successfully');
    } catch (err) {
      setError('Failed to reverse operation. Please try again.');
      console.error('Error reversing operation:', err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="inverter-operations">
      <button
        className="bg-blue-500 text-white h-6 w-6 rounded-sm text-sm flex items-center justify-center disabled:opacity-50"
        onClick={handleClick}
        disabled={isLoading}
        aria-label="Reverse operation"
        title="Reverse operation"
      >
        {isLoading ? (
          <span className="animate-spin">⌛</span>
        ) : (
          <MdCurrencyExchange />
        )}
      </button>    
    </div>
  );
};

export default InverterOperations;