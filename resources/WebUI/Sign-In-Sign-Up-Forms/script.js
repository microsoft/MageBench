const container = document.querySelector(".container");
const headingSpan2 = document.querySelector(".heading-span-2");
const form = document.querySelector(".form");

const clearForm = () => {
  document.querySelectorAll(".form-input-wrapper").forEach((item) => {
    item.className = "form-input-wrapper";
  });
  form.reset();
};

document.querySelector(".signup-btn").addEventListener("click", () => {
  container.classList.add("change");
  setTimeout(() => {
    headingSpan2.textContent = "Up";
  }, 200);
  form.className = "form sign-up";
  clearForm();
});

document.querySelector(".signin-btn").addEventListener("click", () => {
  container.classList.remove("change");
  setTimeout(() => {
    headingSpan2.textContent = "In";
  }, 200);
  form.className = "form sign-in";
  clearForm();
});

const username = document.getElementById("username");
const email = document.getElementById("email");
const password = document.getElementById("password");
const password2 = document.getElementById("password2");

const error = (input, message) => {
  const inputWrapper = input.parentElement;
  inputWrapper.className = "form-input-wrapper error";
  inputWrapper.querySelector(".message").textContent = message;
};

const success = (input) => {
  const inputWrapper = input.parentElement;
  inputWrapper.className = "form-input-wrapper success";
};

const checkEmail = (input) => {
  const regEx = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

  if (regEx.test(input.value.trim())) {
    success(input);
  } else {
    error(input, "Email is not valid");
  }
};

const checkRequiredFields = (inputArr) => {
  inputArr.forEach((input) => {
    if (input.value.trim() === "") {
      if (input.id === "password2") {
        error(input, "Password confirmation is required");
      } else {
        error(input, `${input.id} is required`);
      }
    } else {
      success(input);
    }
  });
};

const checkLength = (input, min, max) => {
  if (input.value.length < min) {
    error(input, `${input.id} must be at least ${min} characters`);
  } else if (input.value.length > max) {
    error(input, `${input.id} must be less than ${max} characters`);
  } else {
    success(input);
  }
};

const passwordsMatch = (input1, input2) => {
  if (input1.value !== input2.value) {
    error(input2, "Passwords do not match");
  }
};

form.addEventListener("submit", (e) => {
  e.preventDefault();

  if (form.classList[1] === "sign-up") {
    checkRequiredFields([username, email, password, password2]);
    checkLength(username, 2, 15);
    checkLength(password, 5, 25);
    passwordsMatch(password, password2);
  } else {
    checkRequiredFields([email, password]);
  }
  checkEmail(email);
});
