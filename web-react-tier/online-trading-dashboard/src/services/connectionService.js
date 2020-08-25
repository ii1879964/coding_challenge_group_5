import axios from 'axios';
 
const api = axios.create({
    baseURL: "http://localhost:8090"
})
 
export default class ConnectionService {
    connectionCheck = async () => {
        const res = await api.post("/connection_check", {})
            .then(response => {
                if(response.status !== 200) {
                    throw new Error(`Couldn't connect to database`);
                }
                return response;
            });
        return res.status;
    }
 
    loginCheck = async (login, password) => {
        const res = await api.post("/login_check", {
            login: login,
            password: password
        }).then(response => response);
        return res.status;
    }
 
    getInstruments = async () => {
        const res = await api.get("/instruments");
        return res.data;
    }
 
    getAveragePrice = async () => {
        const res = await api.get("/instruments/average_price");
        return res.data;
    }
 
    getDealsHistory = async () => {
        const res = await api.get("/deals/history");
        return res.data;
    }
 
    getEndingPosition = async () => {
        const res = await api.get("/instruments/ending_position");
        return res.data;
    }
 
    getRealizedBalance = async () => {
        const res = await api.get("/balance/realized");
        return res.data;
    }
 
    getEffectiveBalance = async () => {
        const res = await api.get("/balance/effective");
        return res.data;
    }
}