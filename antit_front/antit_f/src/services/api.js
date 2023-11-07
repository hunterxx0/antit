import axios from 'axios';

// Setup base URL for your Django backend
const baseURL = 'http://localhost:8000'; // Adjust this URL

const api = axios.create({
  baseURL,
});

//  signup, login

export default api;