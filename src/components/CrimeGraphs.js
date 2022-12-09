import { Bar, Line, Pie } from "react-chartjs-2";
import Chart from "chart.js/auto";
import React from "react";
import crimeData from "../data/crimeData.json";
import { Link } from "react-router-dom";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";

export default function BarGraph() {
  function returnCrimeState() {
    var weaponInfo = {};

    crimeData.features.slice(0, 100).map((crime) => {
      var weapon = crime.properties.Weapon;
      if (weapon !== null) {
        if (!(weapon in weaponInfo)) {
          weaponInfo[weapon] = 0;
        } else if (weapon in weaponInfo) {
          weaponInfo[weapon] += 1;
        }
      }
    });

    console.log(weaponInfo);

    const weaponKeys = Object.keys(weaponInfo);
    const weaponValues = Object.values(weaponInfo);

    const state = {
      labels: weaponKeys,
      datasets: [
        {
          label: "Weapon Bar Graph",
          backgroundColor: "red",
          borderColor: "rgba(0,0,0,1)",
          borderWidth: 2,
          data: weaponValues,
        },
      ],
    };
    return state;
  }

  return (
    <Container maxWidth="lg" align="center">
      <Grid align="center" container>
        <Grid align="center">
          <Typography
            component="h1"
            variant="h2"
            align="center"
            color="text.primary"
            gutterBottom
          >
            Baltimore City Crime Visualizes
          </Typography>
          <Typography
            variant="h5"
            align="center"
            color="text.secondary"
            paragraph
          >
            Displayed underneath is a visualization of the graphs, charts, etc.
            corresponding with Baltimore's crime data. You will see how this
            data is shaped along with insightful information on a visual level.
          </Typography>
          <div>
            <Bar
              data={returnCrimeState()}
              options={{
                title: {
                  display: true,
                  text: "Average Weapon Used Per 100 Crimes",
                  fontSize: 20,
                },
                legend: {
                  display: true,
                  position: "right",
                },
              }}
            />
          </div>
          <div>
            <Line
              data={returnCrimeState()}
              options={{
                title: {
                  display: true,
                  text: "Average Rainfall per month",
                  fontSize: 20,
                },
                legend: {
                  display: true,
                  position: "right",
                },
              }}
            />
          </div>
          <div>
            <Pie
              data={returnCrimeState()}
              options={{
                title: {
                  display: true,
                  text: "Average Rainfall per month",
                  fontSize: 20,
                },
                legend: {
                  display: true,
                  position: "right",
                },
              }}
            />
          </div>
          <div style={{ textAlign: "center" }}>
            <Link to="/crime">Return To Crime Map</Link>
          </div>
        </Grid>
      </Grid>
    </Container>
  );
}
