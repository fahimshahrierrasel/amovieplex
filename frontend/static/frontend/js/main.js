// Now Showing Tab onClick handler
function openNowShowingTab(event, tabDetailId) {
    // Getting all the elements that has same class
    let allTabDetails = document.getElementsByClassName('tab-detail');
    let allTabItems = document.getElementsByClassName('tab-item');

    // Lood through all tab item and remove is active from all
    Array.from(allTabItems).forEach(tabItem => {
        tabItem.className = tabItem.className.replace(' is-active', '');
    })
    // Add is active in current tab which is clicked or generated this event
    event.currentTarget.className += ' is-active';

    // Loop through all tab details id to check if it is matched with selected tab id
    // And change the active and in-active tab accordingly
    Array.from(allTabDetails).forEach(tabDetail => {
        if (tabDetail.id === tabDetailId) {
            tabDetail.className = tabDetail.className.replace(' tab-inactive', '')
        } else {
            tabDetail.className = tabDetail.className.replace(' tab-inactive', '') + ' tab-inactive'
        }
    })
}

// Make nav bar transparent and non trasparent start
let navBar = document.getElementById('navbar');
let topHero = document.getElementById('hero');
let currentChange = 'transparent';
window.onscroll = function() {
    let pagePosition = window.pageYOffset;
    if (pagePosition >= (topHero.clientHeight - navBar.offsetHeight) && currentChange != 'not-transparent') {
        navBar.className = navBar.className.replace(' is-transparent', '');
        navBar.className += ' is-primary';
        navBar.style.backgroundColor = '#00d1b2';
        currentChange = 'not-transparent';
    } else if (pagePosition < (topHero.clientHeight - navBar.offsetHeight) && currentChange != 'transparent') {
        navBar.className = navBar.className.replace(' is-primary', '');
        navBar.className += ' is-transparent'
        currentChange = 'transparent';
        navBar.style = "";
    }
}
// Make nav bar transparent and non trasparent end

// Show comming soon movie details start
function showComingSoonDeatils(item) {
    console.log(item.getAttribute('data-title'));
    document.getElementById('coming_soon_tag').textContent = item.getAttribute('data-tag');
    document.getElementById('coming_soon_name').textContent = item.getAttribute('data-title');
    document.getElementById('coming_soon_details').textContent = item.getAttribute('data-plot');
    document.getElementById('coming_soon_link').href = item.getAttribute('data-link');
    document.getElementById('coming_soon_container').style.backgroundImage = `url(${item.getAttribute('data-img')})`;
}
// Show coming soon movie details end

// Change General Image Start
function changeGeneralImage(item) {
    document.getElementById('image_container').style.backgroundImage = `url(${item.getAttribute('data-img')})`;
}
// Change General Image End

