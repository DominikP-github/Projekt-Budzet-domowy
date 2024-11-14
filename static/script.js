const text = "WIĘCEJ NIŻ ";
const text2 = "aplikacja";
const textElement = document.getElementById("text");
const textElement2 = document.getElementById("text2");
let index = 0;
let index2 = 0;

function typeWriter() {
    if (index < text.length) {
        textElement.innerHTML += text.charAt(index);
        index++;
        setTimeout(typeWriter, 200); 
    } else if (index2 < text2.length) { 
        textElement2.innerHTML += text2.charAt(index2);
        index2++;
        setTimeout(typeWriter, 200); 
    }
}
typeWriter();
document.addEventListener("DOMContentLoaded", function() {
    const items = document.querySelectorAll('.image-item');

    // Funkcja animująca elementy
    const animateItems = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Ujawniamy element
                entry.target.style.opacity = 1; 
                entry.target.style.transform = 'translateY(0)'; // Element przesuwany do pozycji pierwotnej
                
                // Przestajemy obserwować po animacji
                observer.unobserve(entry.target);
            }
        });
    };

    // Ustawienia Intersection Observer
    const observer = new IntersectionObserver(animateItems, {
        threshold: 0.1 // Animacja uruchamia się, gdy 10% elementu jest widoczne
    });

    // Obserwuj każdy element
    items.forEach(item => {
        observer.observe(item);
    });
});


document.addEventListener("DOMContentLoaded", function () {
    const artykul = document.querySelector('.artykul');

    function checkVisibility() {
        const rect = artykul.getBoundingClientRect();
        const windowHeight = (window.innerHeight || document.documentElement.clientHeight);
        
        // Obliczamy środek artykułu
        const artykulCenter = rect.top + rect.height ;
        // Obliczamy środek okna
        const windowCenter = windowHeight ;

        // Sprawdzamy, czy środek elementu jest w środku okna
        if (artykulCenter <= windowCenter && artykulCenter >= 0) {
            artykul.classList.add('visible');
            // Usuwamy listener po dodaniu animacji
            window.removeEventListener('scroll', checkVisibility);
        }
    }

    // Sprawdzaj widoczność przy przewijaniu
    window.addEventListener('scroll', checkVisibility);
    // Sprawdzaj przy załadowaniu strony
    checkVisibility();
});

