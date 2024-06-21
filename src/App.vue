<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router';
import 'boxicons';
import $ from 'jquery';
import {ref} from 'vue';
import { log } from 'console';
import { json } from 'stream/consumers';

window.onresize = () => {
  screen_width_change_event ()
};


let screen_width_change_event = () => { 
  let menu_icon_display = $('#menu_icon').is(':hidden');
  if (menu_icon_display === true) {
    $('nav').show()

  }else{
    $('nav').hide()
  }

}
let SP_Nav_display = () => {
  
  let nav_show = $('nav').is(':hidden');
  
  

  if (nav_show === true ) {
    $('nav').show()
  }else{
    $('nav').hide()
  }
  
}


$(document).ready(function () {
  Get_Store_Data()
})


const store_detail = ref();
const Get_Store_Data = async () =>{

  let api_headers = {
    
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  }
  try {
    let data = await fetch('http://localhost:8000/api/store/',api_headers)
    .then((res)=>{
      
      return res.json()
    })
    
      console.log(data)
      store_detail.value = await data;
  } catch (error) {

    console.log(error)
  }
}









  
</script>

<style lang="scss">

@import '@/assets/css/nav.scss';
@import url('https://fonts.googleapis.com/css2?family=Chocolate+Classical+Sans&display=swap');
</style>
<template>
  <header>
    
    
    <!--store icon-->
    <a href="./home" class="nav_icon">
      <img src="./assets/img/Logo2.PNG" alt=""  id="logo">
    </a>
    <img @click="SP_Nav_display()" src="./assets/img/icons8-menu-150.svg" alt="" width="30" id="menu_icon">

    
    <nav> 
        
      
      <RouterLink to="/home" @click="SP_Nav_display()">首頁 <span>HOME</span></RouterLink>
      <RouterLink to="/about" @click="SP_Nav_display()">關於我們 <span>ABOUT US</span></RouterLink>
      <RouterLink to="/Menu" @click="SP_Nav_display()">菜單 <span>MENU</span></RouterLink>
      <RouterLink to="/address" @click="SP_Nav_display()">門市資訊 <span>BRANCH</span></RouterLink>
      <a href="https://www.chickpt.com.tw/company/k6z0r7ZlmpWD" @click="SP_Nav_display()" target="_blank">徵才資訊 <span>RECRUITS</span></a>
      
    </nav>
    
  </header>

  <main>
    
    <RouterView/>
    
  </main>
  
  <footer>
    <!-- logo -->
    
      

    <div class="footer-logo">
      <img src="./assets/img/changed_logo.png" alt=""  id="footer_logoIMG">
      <div class="footer_store_name">

        <span class="footer_store_name_1">小蒜頭</span>
        <span class="footer_store_name_2">鹹酥雞</span>
      </div>
      
    </div>

    <div class="footer-content">
      <h2>分店資訊</h2>
      <ul v-for="item in store_detail">
        <li>

          分店：{{item.store_name}}

        </li>

        <p>
          地址：{{item.address}}

        </p>
        
        <p>
          電話：{{ item.phone }}
        </p>
      </ul>
    </div>

      

   

    
  </footer>
  
</template>

<style scoped>

</style>
