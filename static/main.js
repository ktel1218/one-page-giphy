$(document).ready(function() {

  var search_terms = [
    "about",
    "above",
    "across",
    "app",
    "apple",
    "appreciate",
    "bad",
    "ball",
    "balloon",
    "bell",
    "cat"
  ];


  var substringMatcher = function(strs) {
    return function findMatches(q, cb) {
      var matches, substringRegex;

      // an array that will be populated with substring matches
      matches = [];

      // regex used to determine if a string contains the substring `q`
      substrRegex = new RegExp(q, 'i');

      // iterate through the pool of strings and for any string that
      // contains the substring `q`, add it to the `matches` array
      $.each(strs, function(i, str) {
        if (substrRegex.test(str)) {
          matches.push(str);
        }
      });

      cb(matches);
    };
  };
  $('input[name="search_term"]').typeahead({
    hint: true,
    highlight: true,
    minLength: 1
  },
  {
    name: 'gifs',
    source: substringMatcher(search_terms)
  });

  console.log("ready!");

  // on form submission ...
  $('form').on('submit', function() {

    console.log("the form has beeen submitted");

    // grab values
    searchTerm = $('input[name="search_term"]').val();
    console.log(searchTerm)

    $.ajax({
      type: "POST",
      url: "/",
      data : { 'search_term': searchTerm},
      success: function(results) {
        // $('input').hide();
        // var randNum = Math.floor(Math.random() * Object.keys(results.items).length)
        console.log(results);
        $('#results').html('<img src="'+results+'">');
        // $('input').val('')
      },
      error: function(error) {
        console.log(error)
      }
    });

  });
});