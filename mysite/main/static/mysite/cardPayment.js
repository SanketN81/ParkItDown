new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
    data() {
      return {
        currentCardBackground: Math.floor(Math.random()* 25 + 1), // just for fun :D
        cardName: "",
        cardNumber: "",
        cardMonth: "",
        cardYear: "",
        cardCvv: "",
        minCardYear: new Date().getFullYear(),
        amexCardMask: "#### ###### #####",
        otherCardMask: "#### #### #### ####",
        cardNumberTemp: "",
        isCardFlipped: false,
        focusElementStyle: null,
        isInputFocused: false
      };
    },
    mounted() {
      this.cardNumberTemp = this.otherCardMask;
      document.getElementById("cardNumber").focus();
    },
    computed: {
      getCardType () {
        let number = this.cardNumber;
        let re = new RegExp("^4");
        if (number.match(re) != null) return "visa";
  
        re = new RegExp("^(34|37)");
        if (number.match(re) != null) return "amex";
  
        re = new RegExp("^5[1-5]");
        if (number.match(re) != null) return "mastercard";
  
        re = new RegExp("^6011");
        if (number.match(re) != null) return "discover";
        
        re = new RegExp('^9792')
        if (number.match(re) != null) return 'troy'
  
        return "visa"; // default type
      },
          generateCardNumberMask () {
              return this.getCardType === "amex" ? this.amexCardMask : this.otherCardMask;
      },
      minCardMonth () {
        if (this.cardYear === this.minCardYear) return new Date().getMonth() + 1;
        return 1;
      }
    },
    watch: {
      cardYear () {
        if (this.cardMonth < this.minCardMonth) {
          this.cardMonth = "";
        }
      }
    },
    methods: {
      flipCard (status) {
        this.isCardFlipped = status;
      },
      focusInput (e) {
        this.isInputFocused = true;
        let targetRef = e.target.dataset.ref;
        let target = this.$refs[targetRef];
        this.focusElementStyle = {
          width: `${target.offsetWidth}px`,
          height: `${target.offsetHeight}px`,
          transform: `translateX(${target.offsetLeft}px) translateY(${target.offsetTop}px)`
        }
      },
      blurInput() {
        let vm = this;
        setTimeout(() => {
          if (!vm.isInputFocused) {
            vm.focusElementStyle = null;
          }
        }, 300);
        vm.isInputFocused = false;
      }
    }
  });
  
  $(".card-form__button").click(function () {
    $(".check-icon").hide();
    setTimeout(function () {
      $(".check-icon").show();
    }, 10);
  });

  $(".card-form__button").click(function () {
    $(".check-icon-1").hide();
    setTimeout(function () {
      $(".check-icon-1").show();
    }, 10);
  });

let paymentSuccess = document.querySelector(".paymentSuccess")
let paymentUnsuccess = document.querySelector(".paymentUnsuccess")
let checkMark = document.querySelector(".success-checkmark")
let cross = document.querySelector(".success-checkmark-1")

function openPaymentResult() {
  let cardNum = document.querySelector("[data-card-num]").value
  let cardNAME = document.querySelector("[data-card-name]").value
  let cardCvv = document.querySelector("[data-card-cvv]").value
  console.log(cardNum.length)
  if ((cardNum.length < 19) || (cardNAME.length < 5) || (cardCvv.length < 3)) {
    paymentUnsuccess.style.visibility = "visible"
    paymentUnsuccess.style.opacity = "1"
    paymentUnsuccess.style.height = "50%"
    paymentUnsuccess.style.width = "40%"
    paymentUnsuccess.style.top = "13em"
    cross.style.visibility = "visible"
    paymentUnsuccess.style.transition = "0.5s"
  } else {
    paymentSuccess.style.visibility = "visible"
    paymentSuccess.style.opacity = "1"
    paymentSuccess.style.height = "50%"
    paymentSuccess.style.width = "40%"
    paymentSuccess.style.top = "13em"
    checkMark.style.visibility = "visible"
    paymentSuccess.style.transition = "0.5s"
  }
  
}

function closeDivToggle() {
  paymentSuccess.style.visibility = "hidden"
  paymentSuccess.style.opacity = "0"
  paymentSuccess.style.height = "0"
  paymentSuccess.style.width = "0"
  paymentSuccess.style.top = "30em"
  checkMark.style.visibility = "hidden"
  paymentSuccess.style.transition = "0.5s"
}

function closeDivToggle1() {
  paymentUnsuccess.style.visibility = "hidden"
  paymentUnsuccess.style.opacity = "0"
  paymentUnsuccess.style.height = "0"
  paymentUnsuccess.style.width = "0"
  paymentUnsuccess.style.top = "30em"
  checkMark.style.visibility = "hidden"
  paymentUnsuccess.style.transition = "0.5s"
}