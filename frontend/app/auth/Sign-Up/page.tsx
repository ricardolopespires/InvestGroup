"use client"

import { ToastContainer, toast } from 'react-toastify';
  import 'react-toastify/dist/ReactToastify.css';
import apiService from "@/services/apiService";
import { useRouter } from "next/navigation";
import { FaSignInAlt } from "react-icons/fa";
import React, { useState } from 'react'
import Image from 'next/image'

import axios from "axios"


const page = () => {

    const router = useRouter();    
    const[formdata, setFormdata] = useState({

        email:"",
        first_name:"",
        last_name:"",
        password:"",
        password2:""       
    })

    const handleOnchange = (e)=>{

        setFormdata({...formdata, [e.target.name]:e.target.value})
        console.log(formdata)
    }


    const handleSubmit = async (e)=>{
    
        e.preventDefault()
        const response = await axios.post('http://localhost:8000/api/v1/auth/register/',formdata)
            console.log(response.data)
            const result=response.data
            if (response.status === 201) {
               router.push("/auth/otp/verify")
               toast.success(result.message)
            }
   
        
      
    }
    
   

  return (
    <section className='flex h-screen justify-center items-center'>
      <ToastContainer />
    <div className='flex flex-col shadow-2xl bg-white rounded min-w-96 p-4'>
       <div className='flex items-center justify-center mb-4 cursor-pointer'>
           <a href="/">
           <Image src={"/images/logo.png"} width={190} height={190} alt='logotipo'/>
           </a>
        </div>
        <hr />
        <div className='p-4 space-y-6'>
        <div className=' space-y-2'>
            <div className="flex items-center w-full space-x-2 ">                
            <span className='text-lg'>SignUp</span>
            </div>
            <p className='font-light text-sm bg-orange-600 text-white p-4 rounded'>
                Entre com as informações para fazer seu cadastro no
                <span className='font-semibold'> EducaOne</span>
            </p>
        </div>
            <form action="" onSubmit={handleSubmit} className="space-y-6 w-full">
            <div className='flex flex-col'>
                 <label htmlFor="" className="text-xs font-semibold">Email Address:</label>
                 <input type="text"
                  className='border rounded py-2 text-xs px-2' 
                  name="email" 
                  value={formdata.email}  
                  onChange={handleOnchange} />
               </div>
               <div className='flex flex-col'>
                 <label htmlFor=""  className="text-xs font-semibold">First Name:</label>
                 <input type="text"
                  className='border rounded py-2 text-xs px-2'
                  name="first_name" 
                  value={formdata.first_name} 
                  onChange={handleOnchange}/>
               </div>
               <div className='flex flex-col'>
                 <label htmlFor=""  className="text-xs font-semibold">Last Name:</label>
                 <input type="text" 
                 className='border rounded py-2 text-xs px-2'
                 name="last_name" 
                 value={formdata.last_name} 
                 onChange={handleOnchange}/>
               </div>
               <div className='flex flex-col'>
                 <label htmlFor=""  className="text-xs font-semibold">Password:</label>
                 <input type="password" 
                 className='border rounded py-2 text-xs px-2' 
                 name="password" 
                 value={formdata.password} 
                 onChange={handleOnchange}/>
               </div>
               <div className='flex flex-col'>
                 <label htmlFor=""  className="text-xs font-semibold">Confirm Password:</label>
                 <input type="password"  
                 className='border rounded py-2 text-xs px-2'  
                 name="password2" 
                 value={formdata.password2} 
                 onChange={handleOnchange}/>
               </div>             
               <div className="w-full">
                 <button type="submit" className="flex items-center justify-center space-x-2 bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded w-full">
                    <span>SignUp</span>
                    <span className="text-2xl">
                    <FaSignInAlt/>
                    </span>
                </button>                 
               </div>
               <div className='flex space-x-2 text-sm'>
               <div className="signup-link">Você já é um membro?</div>
               <a className='text-blue-900' href="/auth/Sign-In">Faça login </a>
               </div>
            </form>      
        </div>
    </div>
</section>
  )
}

export default page