import axios from "axios";

const api = axios.create({
  baseURL: 'http://localhost:8070/sites-man-api',
});

export default api;