import AxiosInstance from "@/services/AxiosInstance";
import { formatNumbers, parseStringify } from "../utils";
import { getUserInfo, UserGetStatus, UserUpdatedStatus } from "./actions.user";




export const getAgents = async (page: number, limit: number) => {

  const response = await AxiosInstance.get(`/api/v1/agents/investment-agents/`);
    if (response.status !== 200) {
        throw new Error("Failed to fetch agents");
    }
    return response.data; 
}