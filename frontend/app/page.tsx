import Navbar from "@/components/home/navbar";
import Hero from "@/components/home/Hero";



export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between ">
      <Navbar/>
      <Hero/>  
    </main>
  );
}
