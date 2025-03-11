"use client"

import { useEffect, useState } from "react"

interface SkillBarProps {
  label: string
  value: number
}

export function SkillBar({ label, value }: SkillBarProps) {
  const [progress, setProgress] = useState(0)

  useEffect(() => {
    const timer = setTimeout(() => {
      setProgress(value)
    }, 100)

    return () => clearTimeout(timer)
  }, [value])

  return (
    <div className="mb-4">
      <div className="mb-1 flex justify-between">
        <span className="text-sm">{label}</span>
        <span className="text-sm">{progress}%</span>
      </div>
      <div className="h-1 w-full bg-[#2e2e38]">
        <div
          className="h-full bg-yellow-500"
          style={{
            width: `${progress}%`,
            transition: "width 1s ease-in-out",
          }}
        ></div>
      </div>
    </div>
  )
}

