import axios from 'axios';

export const ApiService = axios.create({
    // baseURL: import.meta.env.VITE_BE_URL, // PRODUCTION BACKEND URL
    baseURL: import.meta.env.VITE_BE_URL, // DEV BACKEND URL
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
});
