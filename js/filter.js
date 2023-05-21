function myFunction() {
	// Declare variables
	var input, filter, ul, li, a, i, txtValue;
	input = document.getElementById('myInput');
	filter = input.value.toUpperCase();
	ul = document.getElementById("myUL");
	li = ul.getElementsByTagName('li');
  
	// Loop through all list items, and hide those who don't match the search query
	for (i = 0; i < li.length; i++) {
	  a = li[i].getElementsByTagName("a")[0];
	  txtValue = a.textContent || a.innerText;
	  if (txtValue.toUpperCase().indexOf(filter) > -1) {
		li[i].style.display = "";
	  } else {
		li[i].style.display = "none";
	  }
	}
  }

  function myFunction_ov() {
	// Declare variables
	var input, filter, ul, ul2, li, a, i, txtValue;
	input = document.getElementById('myInput2');
	filter = input.value.toUpperCase();
	ul = document.getElementById("myUL");
	ul2 = document.getElementById("myUL2");
	li = ul.getElementsByTagName('li');
	li2 = ul2.getElementsByTagName('li');

	// Loop through all list items, and hide those who don't match the search query
	for (i = 0; i < li.length; i++) {
	  a = li[i].getElementsByTagName("a")[0];
	  txtValue = a.textContent || a.innerText;
	  if (txtValue.toUpperCase().indexOf(filter) > -1) {
		li[i].style.display = "";
	  } else {
		li[i].style.display = "none";
	  }
	}

	for (i = 0; i < li2.length; i++) {
		a = li2[i].getElementsByTagName("a")[0];
		txtValue = a.textContent || a.innerText;
		if (txtValue.toUpperCase().indexOf(filter) > -1) {
		  li2[i].style.display = "";
		} else {
		  li2[i].style.display = "none";
		}
	  }
  }
  