function showLoader(evt)
{ 
    var form = evt.target;
    var loader_button = form.querySelector(".button_with_loader");

    if (!loader_button)
        return;
    
    document.getElementById(loader_button.id).style.display = 'none';

    var loader = document.getElementById(loader_button.id + '_loader');
    loader.style.display = 'table';
    loader.style.visibility = 'visible';
}

function hideLoader(loader_button_id)
{
    document.getElementById(loader_button_id).style.display = 'block';

    var loader = document.getElementById(loader_button_id + '_loader');
    loader.style.display = 'none';
    loader.style.visibility = 'hidden';
}

// Add event listeners to form submit buttons
for (var i = 0; i < document.forms.length; i++)
{
    document.forms[i].addEventListener('submit', function(event) { showLoader(event) } );
}
