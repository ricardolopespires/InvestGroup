import AxiosInstance from "@/services/AxiosInstance";
import { formatNumbers, parseStringify } from "../utils";
import { getUserInfo, UserGetStatus, UserUpdatedStatus } from "./actions.user";




export const getConsultants = async () => {

  const response = await AxiosInstance.get(`/api/v1/agents/investment-agents/`);
    if (response.status !== 200) {
        throw new Error("Failed to fetch agents");
    }
    return response.data; 
}


export const getConsultId = async (id: string) => {
    const response = await AxiosInstance.get(`/api/v1/agents/investment-agents/${id}/`);
    if (response.status !== 200) {
        throw new Error("Failed to fetch agent");
    }
    return response.data;
}

export const getManagers = async () => {

  const response = await AxiosInstance.get(`/api/v1/agents/investment-managers/`);
    if (response.status !== 200) {
        throw new Error("Failed to fetch agents");
    }
    return response.data; 
}

export const getManagerId = async (id: string) => {
  
    const response = await AxiosInstance.get(`/api/v1/agents/investment-managers/${id}/`);
    if (response.status !== 200) {
        throw new Error("Failed to fetch agent");
    }
    return response.data;
};