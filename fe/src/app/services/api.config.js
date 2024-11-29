import axios from 'axios';

export const ApiService = axios.create({
    // baseURL: 'http://localhost:8080/', // PRODUCTION BACKEND URL
    baseURL: 'http://192.168.0.25:5001', // DEV BACKEND URL
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
});
