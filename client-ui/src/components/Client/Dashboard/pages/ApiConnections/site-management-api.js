import axios from "axios";

const api = axios.create({
  baseURL: 'http://localhost:8000/sites-man-api',
});

export default api;