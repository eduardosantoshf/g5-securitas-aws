import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:6869/intrusion-management-api",
});

export default api;