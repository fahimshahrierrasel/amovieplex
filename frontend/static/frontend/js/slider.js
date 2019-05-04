// Main/Big Carousel Initailization 
new Glide('.glide', {
    type: 'carousel',
    autoplay: 5000,
    animationDuration: 3000,
    hoverpause: true
}).mount()

// New In Carousel Initialization start
var before = document.querySelector('#options-peek-before')
var after = document.querySelector('#options-peek-after')

var newInGlide = new Glide('.slider', {
    type: 'carousel',
    startAt: 0,
    perView: 5,
    peek: {
        before: 100,
        after: 100
    }
})

function peek() {
    newInGlide.update({
        peek: {
            before: 100,
            after: 100
        }
    })
}

before.addEventListener('input', peek)
after.addEventListener('input', peek)

newInGlide.mount()
// New In Carousel Initialization end

// Coming soon carousel
let commingSoonSlider = new Glide('.comming-soon-slider', {
    type: 'carousel',
    startAt: 0,
    perView: 5,
    peek: {
        before: 100,
        after: 100
    }
}).mount();