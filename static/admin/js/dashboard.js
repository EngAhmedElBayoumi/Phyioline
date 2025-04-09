document.addEventListener("DOMContentLoaded", function() {
  // // Get the input element by its aria-label or another attribute
  // var inputElement = document.querySelector('input[aria-label="Choose file to upload"]');
  
  // // Change the input type to 'file' if input element exists
  // if (inputElement) {
  //     inputElement.setAttribute('type', 'file');
  // }


  let firstElement = document.querySelector('.font-semibold'); // Selects the first occurrence
  if (firstElement) {
      let parent = firstElement.parentElement; // Gets its first parent
      if (parent) {
          parent.style.cssText = 'height: auto; padding: 20px;';
      }
  }


  // Function to load scripts sequentially
  function loadScript(iframeDoc, src) {
    return new Promise((resolve, reject) => {
      var script = iframeDoc.createElement('script');
      script.type = 'text/javascript';
      script.src = src;
      script.onload = () => resolve();  // Resolve the promise when the script is loaded
      script.onerror = () => reject();  // Reject if there is an error
      iframeDoc.body.appendChild(script);
    });
  }

  // Check if there are iframes in the page
  var iframes = document.getElementsByTagName('iframe');
  if (iframes.length > 0) {
      // Loop through iframes
      for (var i = 0; i < iframes.length; i++) {
        var iframeDoc = iframes[i].contentWindow.document;
        // Ensure iframe body is ready
        if (iframeDoc.body) {
          var head = iframeDoc.createElement('div');
          head.id = 'scripts';
          iframeDoc.body.appendChild(head);

          if (head) {
            console.log("Head exists", head);

            // Array of script sources to be loaded in order
            var scriptsToLoad = [
              "https://code.jquery.com/jquery-3.6.0.min.js",
              "/static/assets/js/jquery-3.6.0.min.js",
              "/static/assets/js/bootstrap.bundle.min.js",
              "/static/assets/js/owl.carousel.min.js",
              "/static/assets/js/lity.min.js",
              "/static/assets/js/jquery.nice-select.min.js",
              "/static/assets/js/datepicker.min.js",
              "/static/assets/js/jquery.timepicker.min.js",
              "/static/assets/js/jquery.magnific-popup.min.js",
              "/static/assets/js/jquery.waypoints.min.js",
              "/static/assets/js/jquery.counterup.min.js",
              "/static/assets/js/main.js",
              "/static/assets/js/ajax-script.js",
            ];

            // Load scripts sequentially using promises
            scriptsToLoad.reduce((promiseChain, scriptSrc) => {
              return promiseChain.then(() => loadScript(iframeDoc, scriptSrc));
            }, Promise.resolve()).then(() => {
              console.log("All scripts loaded successfully.");
            }).catch(err => {
              console.error("Error loading scripts: ", err);
            });
          }
        }
      }
  }
});



document.addEventListener("DOMContentLoaded", function() {
  var iframes = document.getElementsByTagName("iframe");
  if (iframes.length == 0) {
    console.log("iframes not found" );
    return;
  }else{
    console.log("iframes found" );
  }
  // Get the form and the hidden textarea that stores the editor content
  var contentField = document.getElementById("id_content");
  var form = contentField.closest("form");
  console.log("form exist" );

    // check if  there are iframe in the page
  // Assuming GrapesJS is already initialized, hook into the form's submit event
  form.addEventListener("submit", function(event) {
      // Get the GrapesJS editor instance
      var editor = grapesjs.editors[0]; // Assuming it's the first editor instance
      // Extract HTML and CSS using GrapesJS API
      var editorHtml = editor.getHtml();
      var editorCss = editor.getCss();
      // Get the iframe document
      // Combine the HTML and CSS
      var combinedContent = editorHtml + '<style>' + editorCss + '</style>';
      // make contentfield empty
      contentField.value = "";
      // Update the hidden textarea with the editor's current content
      contentField.value = combinedContent;

  });
});

document.addEventListener("DOMContentLoaded", function () {
  // Step 1: Set up a MutationObserver to watch for changes in the DOM
  var observer = new MutationObserver(function (mutationsList) {
    mutationsList.forEach(function (mutation) {
      mutation.addedNodes.forEach(function (addedNode) {
        // Step 2: Check if the added node contains the upload file input
        var uploadFile = addedNode.querySelector && addedNode.querySelector("#gjs-am-uploadFile");
        if (uploadFile) {
          // Step 3: Remove disabled attribute if necessary
          uploadFile.removeAttribute("disabled");

          // Step 4: Add the event listener for file change (user uploads image)
          uploadFile.addEventListener("change", function (event) {
            var file = event.target.files[0]; // Get the uploaded file
            if (file) {
              var formData = new FormData();
              formData.append('file', file);

              // Step 5: Upload the image to the server using AJAX
              fetch('/upload_image/', {
                method: 'POST',
                body: formData,
                headers: {
                  'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value  // Django CSRF token
                }
              })
              .then(response => response.json())
              .then(data => {
                if (data.url) {
                  var imageUrl = data.url;
                  var imageName = file.name;

                  // Step 6 add imageurl to input exit in div with class gjs-field gjs-am-add-field
                  var addimagediv = document.querySelector('.gjs-field.gjs-am-add-field');

                  if (addimagediv) {
                    // get the input element
                    var input = addimagediv.querySelector('input');

                    // set the value of the input element
                    input.value = imageUrl;
                  }

                  
                } else {
                  console.error('Failed to upload image', data.error);
                }
              })
              .catch(error => console.error('Error uploading image:', error));
            }
          });
        }
      });
    });
  });

  // Step 7: Start observing the body for added nodes
  observer.observe(document.body, {
    childList: true, // Watch for direct child nodes being added or removed
    subtree: true    // Watch for nodes added in any descendants
  });
});





