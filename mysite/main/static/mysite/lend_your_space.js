let toggleMenu = document.querySelector('.pop-up');
let popCont1 = document.querySelector('.pop-up-container1');
let popCont2 = document.querySelector('.pop-up-container2');

let toggleMenu1 = document.querySelector('.pop-up-1');
let popCont3 = document.querySelector('.pop-up-container3');
let popCont4 = document.querySelector('.pop-up-container4');

function menuToggle() {
    const toggleMenu = document.querySelector('.menu');
    toggleMenu.classList.toggle('active')
}



function addSpaceToggle() {
    toggleMenu.style.visibility = "visible"
    toggleMenu.style.opacity = "1"
    popCont1.style.opacity = "1"
    popCont2.style.opacity = "1"
    toggleMenu.style.height = "35em"
    toggleMenu.style.width = "70%"
    toggleMenu.style.top = "5em"
    toggleMenu.style.transition = "0.5s"
}

function updateSpaceToggle() {
    toggleMenu1.style.visibility = "visible"
    toggleMenu1.style.opacity = "1"
    popCont3.style.opacity = "1"
    popCont4.style.opacity = "1"
    toggleMenu1.style.height = "35em"
    toggleMenu1.style.width = "70%"
    toggleMenu1.style.top = "5em"
    toggleMenu1.style.transition = "0.5s"
   // clickeddata(this)
}

function closeDivToggle() {
    toggleMenu.style.visibility = "hidden"
    toggleMenu.style.opacity = "0"
    popCont1.style.opacity = "0"
    popCont2.style.opacity = "0"
    toggleMenu.style.height = "0"
    toggleMenu.style.width = "0"
    toggleMenu.style.top = "30em"
    toggleMenu.style.transition = "0.5s"

    toggleMenu1.style.visibility = "hidden"
    toggleMenu1.style.opacity = "0"
    popCont3.style.opacity = "0"
    popCont4.style.opacity = "0"
    toggleMenu1.style.height = "0"
    toggleMenu1.style.width = "0"
    toggleMenu1.style.top = "30em"
    toggleMenu1.style.transition = "0.5s"
}

const parkingImg1 = document.getElementById('parkingImg-1');
const previewContainer1 = document.getElementById('imagePreview-1');
const previewImage1 = previewContainer1.querySelector('.image-preview__image-1');
const previewDefaultText1 = previewContainer1.querySelector('.image-preview__default-text-1')

parkingImg1.addEventListener("change", function() {
    const file = this.files[0];

    if (file) {
        const reader = new FileReader();

        previewDefaultText1.style.display = "none";
        previewImage1.style.display = "block";

        reader.addEventListener("load", function() {
            console.log(this);
            previewImage1.setAttribute("src", this.result);
        });

        reader.readAsDataURL(file);
    } else {
        previewDefaultText1.style.display =null;
        previewImage1.style.display = null;
        previewImage1.setAttribute("src", "");

    }
});


const parkingImg2 = document.getElementById('parkingImg-2');
const previewContainer2 = document.getElementById('imagePreview-2');
const previewImage2 = previewContainer2.querySelector('.image-preview__image-2');
const previewDefaultText2 = previewContainer2.querySelector('.image-preview__default-text-2')

parkingImg2.addEventListener("change", function() {
    const file = this.files[0];

    if (file) {
        const reader = new FileReader();

        previewDefaultText2.style.display = "none";
        previewImage2.style.display = "block";

        reader.addEventListener("load", function() {
            console.log(this);
            previewImage2.setAttribute("src", this.result);
        });

        reader.readAsDataURL(file);
    } else {
        previewDefaultText2.style.display =null;
        previewImage2.style.display = null;
        previewImage2.setAttribute("src", "");

    }
});