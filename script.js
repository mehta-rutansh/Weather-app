const API_KEY = "YOUR_API_KEY_HERE"; // Replace with your OpenWeatherMap API Key

async function getWeather() {
  const city = document.getElementById('cityInput').value;
  const resultDiv = document.getElementById('weatherResult');
  const errorDiv = document.getElementById('error');

  resultDiv.innerHTML = "";
  errorDiv.innerText = "";

  if (!city) {
    errorDiv.innerText = "Please enter a city name.";
    return;
  }

  try {
    const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`);

    if (!response.ok) {
      throw new Error("City not found");
    }

    const data = await response.json();
    const { main, weather, name } = data;

    const html = `
      <h2>${name}</h2>
      <p><strong>${weather[0].main}</strong> - ${weather[0].description}</p>
      <p>🌡️ Temperature: ${main.temp}&deg;C</p>
      <p>💧 Humidity: ${main.humidity}%</p>
    `;
    resultDiv.innerHTML = html;

    saveDataAsJSON(name, main.temp, main.humidity, weather[0].main);
  } catch (err) {
    errorDiv.innerText = err.message;
  }
}

function saveDataAsJSON(city, temp, humidity, condition) {
  const weatherData = {
    city,
    temperature: temp,
    humidity,
    condition,
    fetched_at: new Date().toISOString()
  };

  const blob = new Blob([JSON.stringify(weatherData, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = `${city}-weather.json`;
  a.click();

  URL.revokeObjectURL(url);
}
