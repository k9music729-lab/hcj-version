// Background image changer
const images = ["image1.jpg", "image2.jpg", "image3.jpg"];
const bgImage = document.querySelector(".background_content");
let index = 0;

setInterval(() => {
  index = (index + 1) % images.length;
  bgImage.src = images[index];
}, 5000);

// OpenRouter API call
document.getElementById("chatForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const prompt = document.getElementById("name").value;

  const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": "Bearer YOUR_API_KEY", // Replace with your actual key (⚠️ don't expose this in production)
      "Content-Type": "application/json",
      "HTTP-Referer": "http://localhost",  // optional
      "X-Title": "BakchodiBot"
    },
    body: JSON.stringify({
      model: "cognitivecomputations/dolphin-mistral-24b-venice-edition:free",
      messages: [{ role: "user", content: prompt }]
    })
  });

  const data = await response.json();
  alert(data.choices[0].message.content);
});
