// eslint-disable-next-line no-unused-vars
import React, { useEffect, useRef } from "react";
import { AiFillBackward } from "react-icons/ai";
import Map from "ol/Map";
import View from "ol/View";
import TileLayer from "ol/layer/Tile";
import OSM from "ol/source/OSM";
import "./map.css";
import "ol/ol.css";
import { Link } from "react-router-dom";

const MapComponent = () => {
  const mapRef = useRef(null);

  useEffect(() => {
    const olMap = new Map({
      target: mapRef.current, // Use the ref as the target element for the map
      view: new View({
        center: [0, 0],
        zoom: 3,
      }),
      layers: [
        new TileLayer({
          source: new OSM(),
        }),
      ],
    });

    return () => {
      // Clean up the map when the component is unmounted
      olMap.setTarget(null);
    };
  }, []);

  return (
    <>
      <div className="map-container container">
        <Link to="/">
          <div className="home center">
            <AiFillBackward />
            <h2>Back to home</h2>
          </div>
        </Link>
        <div ref={mapRef} className="openmap"></div>
      </div>
    </>
  );
};

export default MapComponent;
