import axios from "axios";

const api = axios.create({
  //baseURL: "http://localhost:6869/intrusion-management-api",
  baseURL: process.env.REACT_APP_INTRUSION_MANAGEMENT_API_URL,
});

export default api;