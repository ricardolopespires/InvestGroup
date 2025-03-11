import { ChevronRight } from "lucide-react"

interface ServiceCardProps {
  title: string
  description: string
}

export function ServiceCard({ title, description }: ServiceCardProps) {
  return (
    <div className="group flex flex-col bg-[#2e2e38] p-6 transition-all hover:bg-yellow-500 hover:text-black">
      <h3 className="mb-4 text-xl font-semibold">{title}</h3>
      <p className="mb-6 text-sm group-hover:text-black/80">{description}</p>
      <a href="#" className="mt-auto flex items-center text-sm font-medium text-yellow-500 group-hover:text-black">
        ORDER NOW <ChevronRight className="ml-1 h-4 w-4" />
      </a>
    </div>
  )
}

