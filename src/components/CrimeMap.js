import Container from "@mui/material/Container";
import React, { useState } from "react";
import Button from "@mui/material/Button";
import HeatmapLayer from "react-leaflet-heatmap-layer";
import Grid from "@mui/material/Grid";
import { Map, Marker, Popup, TileLayer } from "react-leaflet";
import crimeData from "../data/crimeData.json";
import Typography from "@mui/material/Typography";
import "leaflet.heat";

export default function MapDisplay() {
  const [dataPoints, setDataPoints] = useState([]);
  const [crimeInfo, setCrimeInfo] = useState([]);

  function toggleHeatMap() {
    if (dataPoints.length === 0) {
      var heatMapPoints = [];
      crimeData.features.map((crime) => {
        let data = {
          coordinates: [crime.properties.Longitude, crime.properties.Latitude],
        };
        heatMapPoints.push(data);
      });
      setDataPoints(heatMapPoints);
    } else {
      setDataPoints([]);
    }
  }

  function toggleCrimeInfo() {
    if (crimeInfo.length === 0) {
      setCrimeInfo(crimeData.features);
    } else {
      setCrimeInfo([]);
    }
  }

  return (
    <Container style={{ marginTop: 80 }} maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Grid container spacing={3}>
        <Grid align="center" item xs={12} md={8} lg={9}>
          <Map center={[39.2904, -76.6122]} zoom={13} scrollWheelZoom={false}>
            <HeatmapLayer
              points={dataPoints}
              longitudeExtractor={(m) => m.coordinates[0]}
              latitudeExtractor={(m) => m.coordinates[1]}
              intensityExtractor={(m) => 100}
            />
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetuseMap</a> contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {crimeInfo.slice(0, 100).map((crime) =>
              crime.properties.Latitude != null &&
              crime.properties.Longitude != null ? (
                <Marker
                  key={crime.properties.RowID}
                  position={[
                    crime.properties.Latitude,
                    crime.properties.Longitude,
                  ]}
                >
                  <Popup>
                    Crime Description: {crime.properties.Description} <br />
                    Location: {crime.properties.Location} <br />
                    Time: {crime.properties.CrimeDateTime} <br />
                    Weapon: {crime.properties.Weapon} <br />
                    Race: {crime.properties.Race} <br />
                    Gender: {crime.properties.Gender} <br />
                    Age: {crime.properties.Age} <br />
                  </Popup>
                </Marker>
              ) : (
                <p></p>
              ),
            )}
          </Map>
        </Grid>
      </Grid>
      <div style={{ paddingTop: " 1.0em", textAlign: "center" }}>
        <Button onClick={toggleHeatMap} variant="outlined">
          Toggle Heat Map
        </Button>
        <Button onClick={toggleCrimeInfo} variant="outlined">
          Toggle Data Points
        </Button>
        <Button variant="outlined" href="/crime-graphs">
          Display Crime Graphs
        </Button>
      </div>
    </Container>
  );
}
