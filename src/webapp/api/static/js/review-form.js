const NON_LIST_FORM_LABELS = ["name", "rating", "tagline", "review", "city", "country"]
const LIST_FORM_LABELS = ["types", "coordinates"];

window.addEventListener('load', function () {
    const review_button = document.getElementById("review-form-submit-button");

    review_button.addEventListener("click", async function () {
        const reviewForm = document.getElementById("review-form");
        const reviewFormElements = document.getElementById("review-form").elements;
        responseCode = await executeRequest(reviewFormElements);

        if (responseCode == "200") {
            reviewForm.append("Review post suceeded");
        } else {
            reviewForm.append("Review post failed");
        }

        reviewForm.reset();
    });
  })

function executeRequest(formElements) {
    var data = {}
    NON_LIST_FORM_LABELS.forEach(function mapFormElementsToRequest(inputName) {
        var input = formElements[inputName].value;
        if (input) {
            data[inputName] = input
        }
    })

    LIST_FORM_LABELS.forEach(function mapListFormElementsToRequest(inputName) {
        var input = formElements[inputName].value;
        if (input) {
            type_list = formElements[inputName].value.split(", ")
            data[inputName] = type_list
        }
    })

    const jsonPayload = JSON.stringify(data);

    const responseStatus = fetch('/place', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: jsonPayload
      })
      .then(response => response.status)
    
      return responseStatus
}

