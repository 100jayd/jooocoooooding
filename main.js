// Initialize Dashboard Interactions
document.addEventListener("DOMContentLoaded", () => {
  console.log("TSLA & PLTR Tracker initialized successfully.");
  console.log("Widgets are loaded from TradingView via external embedding.");

  // Example: Add a subtle entry animation to the cards
  const cards = document.querySelectorAll('.stock-card');
  
  cards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    
    setTimeout(() => {
      card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
      card.style.opacity = '1';
      card.style.transform = 'translateY(0)';
      
      // Remove transition after animation to allow hover effects to work correctly
      setTimeout(() => {
        card.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
      }, 600);
      
    }, 150 * (index + 1)); // Stagger the animation
  });
});
