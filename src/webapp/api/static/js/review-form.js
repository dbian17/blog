const NON_LIST_PLACE_DATA_FORM_LABELS = ["name", "rating", "tagline", "city", "country"]
const LIST_PLACE_DATA_FORM_LABELS = ["types", "coordinates"];
const REVIEW_FORM_LABELS = ["name", "review"]

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
    const placeDataPayload = getPlaceDataPayload(formElements)
    const placeReviewPayload = getPlaceReviewPayload(formElements)

    data['place_data'] = placeDataPayload
    data['place_review'] = placeReviewPayload

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

function getPlaceDataPayload(formElements) {
    const placeDataPayload = {}
    NON_LIST_PLACE_DATA_FORM_LABELS.forEach(function mapFormElementsToRequest(inputName) {
        var input = formElements[inputName].value;
        if (input) {
            placeDataPayload[inputName] = input
        }
    })

    LIST_PLACE_DATA_FORM_LABELS.forEach(function mapListFormElementsToRequest(inputName) {
        var input = formElements[inputName].value;
        if (input) {
            type_list = formElements[inputName].value.split(", ")
            placeDataPayload[inputName] = type_list
        }
    })

    return placeDataPayload
}

function getPlaceReviewPayload(formElements) {
    const placeReviewPayload = {}

    REVIEW_FORM_LABELS.forEach(function mapFormElementsToRequest(inputName) {
        var input = formElements[inputName].value;
        if (input) {
            placeReviewPayload[inputName] = input
        }
    })

    return placeReviewPayload
}

