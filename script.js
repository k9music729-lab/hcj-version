// Background image changer
const images = ["image1.jpg", "image2.jpg", "image3.jpg"];
const bgImage = document.querySelector(".background_content");
let index = 0;

setInterval(() => {
  index = (index + 1) % images.length;
  bgImage.src = images[index];
}, 5000);

// Submit handler
document.getElementById("chatForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const prompt = document.getElementById("name").value;

  try {
    const response = await fetch("https://hcj-version.onrender.com/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ prompt: prompt })
    });

    const data = await response.json();
    alert(data.response);  // Adjust this depending on your backend JSON format
  } catch (error) {
    alert("Error: " + error.message);
  }
});
