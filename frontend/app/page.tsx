import Accordion from "@/components/home/Accordion";
import Assessment from "@/components/home/assessment";
import Compliance from "@/components/home/Compliance";
import Features from "@/components/home/Features";
import Footer from "@/components/home/Footer";
import Hero from "@/components/home/Hero";
import Indicators from "@/components/home/Indicators";
import Newsletter from "@/components/home/Newsletter";
import Prices from "@/components/home/Prices";
import Responsive from "@/components/home/Responsive";
import Tracking from "@/components/home/Tracking";
import WhyChoose from "@/components/home/WhyChoose";

export default function Home() {
  return (
    <div className="overflow-hidden ">
      <Responsive/>
      <Hero/>
      <WhyChoose/>
      <Tracking/> 
      <Indicators/>          
      <Compliance/>
      <Prices/>
      <Accordion/>
      <Assessment/>
     
      <Footer/>
    </div>
  );
}
