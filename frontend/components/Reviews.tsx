"use client"

import type React from "react"

import { Star, StarHalf, X } from "lucide-react"
import { useState } from "react"
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription } from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

export default function Reviews({Asset}:{Asset:string}) {
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [rating, setRating] = useState(0)
  const [hoveredRating, setHoveredRating] = useState(0)
  const [reviewText, setReviewText] = useState("")
  const [name, setName] = useState("")

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // Here you would typically send the review data to your backend
    console.log({ name, rating, reviewText })
    // Reset form and close modal
    setRating(0)
    setReviewText("")
    setName("")
    setIsModalOpen(false)
  }

  return (
    <div >
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {/* Average Rating Section */}
        <div className="bg-white p-6 rounded-lg shadow-sm border">
          <h2 className="text-2xl font-bold mb-6">Average Rating</h2>

          <div className="flex items-center gap-4 mb-6">
            <span className="text-4xl font-bold">4.5</span>
            <div>
              <div className="flex text-amber-400 mb-1">
                <Star className="fill-amber-400 w-5 h-5" />
                <Star className="fill-amber-400 w-5 h-5" />
                <Star className="fill-amber-400 w-5 h-5" />
                <Star className="fill-amber-400 w-5 h-5" />
                <StarHalf className="fill-amber-400 w-5 h-5" />
              </div>
              <span className="text-gray-500">50k Reviews</span>
            </div>
          </div>

          <div className="space-y-2 mb-8">
            <div className="flex items-center gap-2">
              <span className="w-4 text-right">5</span>
              <div className="h-5 bg-gray-200 rounded-full flex-1">
                <div className="h-5 bg-orange-400 rounded-full" style={{ width: "90%" }}></div>
              </div>
              <span className="w-8 text-right text-gray-500">90%</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="w-4 text-right">4</span>
              <div className="h-5 bg-gray-200 rounded-full flex-1">
                <div className="h-5 bg-orange-400 rounded-full" style={{ width: "60%" }}></div>
              </div>
              <span className="w-8 text-right text-gray-500">60%</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="w-4 text-right">3</span>
              <div className="h-5 bg-gray-200 rounded-full flex-1">
                <div className="h-5 bg-orange-400 rounded-full" style={{ width: "40%" }}></div>
              </div>
              <span className="w-8 text-right text-gray-500">40%</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="w-4 text-right">2</span>
              <div className="h-5 bg-gray-200 rounded-full flex-1">
                <div className="h-5 bg-orange-400 rounded-full" style={{ width: "30%" }}></div>
              </div>
              <span className="w-8 text-right text-gray-500">30%</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="w-4 text-right">1</span>
              <div className="h-5 bg-gray-200 rounded-full flex-1">
                <div className="h-5 bg-orange-400 rounded-full" style={{ width: "2%" }}></div>
              </div>
              <span className="w-8 text-right text-gray-500">0%</span>
            </div>
          </div>

          <div className="mt-6">
            <h3 className="text-lg font-semibold mb-3">Escreva sua avaliação</h3>
            <p className="text-gray-500 mb-4">
              Compartilhe seu feedback e ajude a criar uma melhor experiência de compra para todos..
            </p>
            <button
              onClick={() => setIsModalOpen(true)}
              className="bg-orange-400 hover:bg-orange-500 text-white font-medium py-2 px-6 rounded-md transition-colors"
            >
              Enviar avaliações
            </button>
          </div>
        </div>

        {/* Customer Feedback Section */}
        <div>
          <h2 className="text-2xl font-bold mb-6">Feedback do cliente</h2>

          <div className="space-y-6">
            {/* Review 1 */}
            <div className="bg-white p-6 rounded-lg shadow-sm border">
              <div className="flex justify-between mb-3">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-sky-200 flex items-center justify-center">
                    <span className="text-sky-500 text-xl">R</span>
                  </div>
                  <div>
                    <h3 className="font-semibold">Rachel Patel</h3>
                    <p className="text-gray-500 text-sm">October 5, 2023</p>
                  </div>
                </div>
                <div className="flex text-amber-400">
                  <Star className="fill-amber-400 w-5 h-5" />
                  <Star className="fill-amber-400 w-5 h-5" />
                  <Star className="fill-amber-400 w-5 h-5" />
                  <Star className="fill-amber-400 w-5 h-5" />
                  <Star className="fill-amber-400 w-5 h-5" />
                </div>
              </div>
              <p className="text-gray-600">
                Couldn't resist buying this watch after seeing it online, and I'm so glad I did. It's even more stunning
                in person, and the build quality is exceptional. Will definitely be purchasing from this brand again!
              </p>
            </div>

            {/* Review 2 */}
            <div className="bg-white p-6 rounded-lg shadow-sm border">
              <div className="flex justify-between mb-3">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-purple-200 flex items-center justify-center">
                    <span className="text-purple-500 text-xl">C</span>
                  </div>
                  <div>
                    <h3 className="font-semibold">Christopher Lee</h3>
                    <p className="text-gray-500 text-sm">June 25, 2023</p>
                  </div>
                </div>
                <div className="flex text-amber-400">
                  <Star className="fill-amber-400 w-5 h-5" />
                  <Star className="fill-amber-400 w-5 h-5" />
                  <Star className="fill-amber-400 w-5 h-5" />
                  <Star className="fill-amber-400 w-5 h-5" />
                  <StarHalf className="fill-amber-400 w-5 h-5" />
                </div>
              </div>
              <p className="text-gray-600">
                Really impressed with the quality and style of this watch. It's exactly what I was looking for –
                versatile, durable, and looks great with any outfit. Docked half a star because the clasp is a bit
                tricky to open, but otherwise, it's perfect!
              </p>
            </div>

            {/* Review 3 */}
            <div className="bg-white p-6 rounded-lg shadow-sm border">
              <div className="flex justify-between mb-3">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-red-200 flex items-center justify-center">
                    <span className="text-red-500 text-xl">B</span>
                  </div>
                  <div>
                    <h3 className="font-semibold">Brian Chen</h3>
                    <p className="text-gray-500 text-sm">April 15, 2022</p>
                  </div>
                </div>
                <div className="flex text-amber-400">
                  <Star className="fill-amber-400 w-5 h-5" />
                  <Star className="fill-amber-400 w-5 h-5" />
                  <Star className="fill-amber-400 w-5 h-5" />
                  <Star className="fill-amber-400 w-5 h-5" />
                  <Star className="w-5 h-5 text-gray-300" />
                </div>
              </div>
              <p className="text-gray-600">
                While this watch has its merits, such as its sleek design and comfortable wear, I found the strap to be
                somewhat flimsy, and the clasp occasionally difficult to secure. Despite these minor drawbacks, it does
                keep accurate time.
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Review Submission Modal */}
      <Dialog open={isModalOpen} onOpenChange={setIsModalOpen}>
        <DialogContent className="sm:max-w-[500px]">
          <DialogHeader>
            <div className="flex items-center justify-between">
              <DialogTitle>Escreva uma avaliação</DialogTitle>
              <Button variant="ghost" size="icon" onClick={() => setIsModalOpen(false)}>
                <X className="h-4 w-4" />
              </Button>
            </div>
            <DialogDescription>
              Compartilhe sua experiência com este produto. Sua avaliação ajudará outros compradores.
            </DialogDescription>
          </DialogHeader>

          <form onSubmit={handleSubmit} className="space-y-4 mt-4">
            <div className="space-y-2">
              <Label htmlFor="rating">Avaliação</Label>
              <div className="flex gap-1">
                {[1, 2, 3, 4, 5].map((star) => (
                  <button
                    key={star}
                    type="button"
                    onClick={() => setRating(star)}
                    onMouseEnter={() => setHoveredRating(star)}
                    onMouseLeave={() => setHoveredRating(0)}
                    className="focus:outline-none"
                  >
                    <Star
                      className={`w-8 h-8 ${
                        (hoveredRating ? star <= hoveredRating : star <= rating)
                          ? "fill-amber-400 text-amber-400"
                          : "text-gray-300"
                      }`}
                    />
                  </button>
                ))}
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="name">Seu nome (opcional)</Label>
              <Input id="name" value={name} onChange={(e) => setName(e.target.value)} placeholder="Enter your name" />
            </div>

            <div className="space-y-2">
              <Label htmlFor="review">Sua avaliação</Label>
              <Textarea
                id="review"
                value={reviewText}
                onChange={(e) => setReviewText(e.target.value)}
                placeholder="What did you like or dislike? What did you use this product for?"
                rows={5}
                required
              />
            </div>

            <div className="flex justify-end gap-3 pt-3">
              <Button type="button" variant="outline" onClick={() => setIsModalOpen(false)}>
                Cancel
              </Button>
              <Button
                type="submit"
                className="bg-orange-400 hover:bg-orange-500 text-white"
                disabled={rating === 0 || !reviewText.trim()}
              >
                Submit Review
              </Button>
            </div>
          </form>
        </DialogContent>
      </Dialog>
    </div>
  )
}
