document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('toggle_header').addEventListener('click', function() {
        if (document.querySelector('header').classList.contains('red')) {
            document.querySelector('header').classList.remove('red');
            document.querySelector('header').classList.add('green');
        } else if (document.querySelector('header').classList.contains('green')) {
            document.querySelector('header').classList.remove('green');
            document.querySelector('header').classList.add('red');
        }}
    );
}
);