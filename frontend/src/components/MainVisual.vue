<template>
  <main id="main">
    <section class="process">
      <!-- <div class="inner"> -->
      <div class="wine-font">
        <div class="main-font">
          <p>당신이</p>
          <p>찾던</p>
          <p><b>와인서비스</b></p>
        </div>
        <div class="sub-font">
          <strong
            >이제부터는 찾지마세요.<br />
            기록하세요.<br />
            고객님의 취향에 맞는 와인을 빠르고 신속하게 <br />추천해주는
            시스템입니다.</strong
          >
        </div>
        <div class="btn-class">
          <button>와인 추천받으러 가기</button>
          <button>서비스 소개</button>
        </div>
      </div>
      <!-- </div> -->
    </section>
  </main>
</template>

<style lang="scss">
@import "@/assets/scss/reset";
@import url("https://fonts.googleapis.com/css2?family=Yellowtail&display=swap");

@-webkit-keyframes slide-in-top {
  0% {
    -webkit-transform: translateY(-1000px);
    transform: translateY(-1000px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
    opacity: 1;
  }
}
@keyframes slide-in-top {
  0% {
    -webkit-transform: translateY(-1000px);
    transform: translateY(-1000px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
    opacity: 1;
  }
}

.wine-font {
  width: 1436px;
  margin: 130px auto;
  text-align: right;
}

.wine-font p {
  font-size: 70px;
  font-weight: bold;
  color: darkblue;
  animation: slide-in-top 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}

.wine-font p b {
  color: #840435;
}

.sub-font {
  font-size: 16px;
  margin-top: 20px;
  color: #840435;
  text-align: right;
  animation: slide-in-top 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}

.btn-class {
  margin-top: 30px;
  display: flex;
  gap: 20px;
  flex-direction: row-reverse;
  animation: slide-in-top 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}

button {
  border: none;
  display: inline-block;
  padding: 15px 30px;
  border-radius: 15px;
  font-family: "paybooc-Light", sans-serif;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
  text-decoration: none;
  font-weight: 600;
  transition: 0.25s;
  cursor: pointer;
}

button:hover {
  color: #1e6b7b;
  background: aliceblue;
  transform: scale(1.1);
}
</style>
