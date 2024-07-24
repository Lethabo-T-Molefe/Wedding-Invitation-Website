document.addEventListener('DOMContentLoaded', () => {
  const rsvpForm = document.getElementById('rsvp-form');
  rsvpForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const attending = document.getElementById('attending').value;
    if (name && attending) {
      alert(`Thank you, ${name}, for your RSVP. You have selected to ${attending === 'yes' ? 'attend' : 'not attend'} the wedding.`);
      rsvpForm.reset();
    }
  });
});

$(window).scroll(function() {
            if ($(document).scrollTop() > 50) {
                $('.nav').addClass('affix');
                console.log("OK");
            } else {
                $('.nav').removeClass('affix');
            }
});

function submitAlert() {
  alert("Form submitted!");
}

$('.navTrigger').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();

});

document.getElementById('search').addEventListener('keyup', function () {
  var searchTerm = this.value.toLowerCase();
  var tables = document.querySelectorAll('table tbody');
  tables.forEach(function (tbody) {
    var rows = tbody.querySelectorAll('tr');
    rows.forEach(function (row) {
      var cells = row.querySelectorAll('td');
      var found = Array.from(cells).some(function (cell) {
        return cell.textContent.toLowerCase().includes(searchTerm);
      });
      row.style.display = found ? '' : 'none';
    });
  });
});