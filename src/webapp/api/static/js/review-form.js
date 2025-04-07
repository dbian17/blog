const NON_TYPE_FORM_LABELS = ["name", "rating", "tagline", "review"]
const TYPE_FORM_LABEL = "types";

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
    });
  })

function executeRequest(formElements) {
    var data = {}
    NON_TYPE_FORM_LABELS.forEach(function mapFormElementsToRequest(inputName) {
        var input = formElements[inputName].value;
        if (input) {
            data[inputName] = input
        }
    })

    if (formElements[TYPE_FORM_LABEL].value) {
        type_list = formElements[TYPE_FORM_LABEL].value.split(" ")
        data[TYPE_FORM_LABEL] = type_list
    }

    const jsonPayload = JSON.stringify(data);

    const responseStatus = fetch('https://blog-azure-seven-70.vercel.app/place', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: jsonPayload
      })
      .then(response => response.status)
    
      return responseStatus
}

