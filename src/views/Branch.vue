<script setup lang="ts">
import 'animate.css';
import "@/assets/css/branch.scss";

import 'bootstrap/dist/css/bootstrap.min.css';
import { onMounted, ref } from 'vue';
import 'animate.css';
import $ from 'jquery';



let histroy: any = [{
    "TIME": "民國82年/8月",
    "DESCRIPTION": "成立於台南市長榮路一段（新崇安戲院旁）",
    "PICTURE": new URL("@/assets/img/東安戲院.jpg", import.meta.url).href
},
{
    "TIME": "民國82年/10月",
    "DESCRIPTION": "搬遷至台南縣歸仁（中正路與復興路口）",
    "PICTURE": new URL("@/assets/img/歸仁店.svg", import.meta.url).href
},
{
    "TIME": "民國85年",
    "DESCRIPTION": "台南關廟第一家分店成立（民國111年閉幕)",
    "PICTURE": ""
},
{
    "TIME": "民國92年",
    "DESCRIPTION": "台南新化店分店成立",
    "PICTURE": new URL("@/assets/img/新化分店.svg", import.meta.url).href
},
{
    "TIME": "民國113年",
    "DESCRIPTION": "台南新關廟店成立",
    "PICTURE": new URL("@/assets/img/關廟新店.jpg", import.meta.url).href
},

]


</script>
<style lang="scss"></style>
<template>


    <div class="">
        <h1 class="home_title">分店據點 Branch</h1>
    </div>

    <div class="introducions">

        <div class="branch_block">
            <div class="col-lg-4">
                <iframe
                    src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d14694.339678250059!2d120.2942227!3d22.965509!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x346e71e603fd6cfb%3A0x6301298435e544f5!2z5bCP6JKc6aCt6bm96YWl6ZueKOatuOS7geW6lyk!5e0!3m2!1szh-TW!2stw!4v1721385290670!5m2!1szh-TW!2stw"
                    width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"
                    referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
            <div class="col-lg-8">
                <h4> 歸仁店 (總店) </h4>


                <h4>地址:</h4>
                <p> 台南市歸仁區中正南路(總店)</p>
                <h4>營業時間:</h4>
                <ul>
                    <li>
                        周一 17:00 ~ 23:00
                    </li>
                    <li>周二 17:00 ~ 23:00</li>
                    <li>周三 公休</li>
                    <li>周四 公休</li>
                    <li>周五 17:00 ~ 23:30 </li>
                    <li>周六 17:00 ~ 23:30 </li>
                    <li>周日 17:00 ~ 23:00</li>
                </ul>



            </div>
        </div>

        <div class="branch_block">
            <div class="col-lg-4">
                <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d14686.68578932631!2d120.3078521!3d23.0358327!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x346e713b4e78ccd1%3A0xa70f135a4d7db78d!2z5bCP6JKc6aCt6bm96YWl6Zue5paw5YyW!5e0!3m2!1szh-TW!2stw!4v1721713527273!5m2!1szh-TW!2stw" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
            <div class="col-lg-8">
                <h4> 新化店 </h4>


                <h4>地址:</h4>
                <p> 台南市新化區中山路255號</p>
                <h4>營業時間:</h4>
                <ul>
                    <li>
                        周一 公休
                    </li>
                    <li>周二 公休</li>
                    <li>周三 17:00 ~ 23:00</li>
                    <li>周四 17:00 ~ 23:00</li>
                    <li>周五 17:00 ~ 23:00 </li>
                    <li>周六 17:00 ~ 23:00 </li>
                    <li>周日 17:00 ~ 23:00</li>
                </ul>

            </div>

        </div>

        <div class="branch_block">
            <div class="col-lg-4">
                <iframe
                    src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d14694.339678250059!2d120.2942227!3d22.965509!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x346e71e603fd6cfb%3A0x6301298435e544f5!2z5bCP6JKc6aCt6bm96YWl6ZueKOatuOS7geW6lyk!5e0!3m2!1szh-TW!2stw!4v1721385290670!5m2!1szh-TW!2stw"
                    width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"
                    referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
            <div class="col-lg-8">
                <h4> 關廟店 </h4>


                <h4>地址:</h4>
                <p> 718台南市關廟區中正路749號</p>
                <h4>營業時間:</h4>
                <ul>
                    <li>
                        周一 16:30 ~ 23:00
                    </li>
                    <li>周二 16:30 ~ 23:00</li>
                    <li>周三 16:30 ~ 23:00</li>
                    <li>周四 16:30 ~ 23:00</li>
                    <li>周五 16:30 ~ 23:30 </li>
                    <li>周六 16:30 ~ 23:30 </li>
                    <li>周日 16:30 ~ 23:00</li>
                </ul>

            </div>

        </div>
    </div>


    <div class="second container-fluid row m-0 p-0">

        <div class="col-lg-12 history">

            <h1 class="wow animate__animated animate__fadeIn">門市故事</h1>


            <div class="arrow"></div>


            <div class="history_text">

                <!--1-->

                <div v-for="item in histroy" :key="item" class="history_group">


                    <p class="history_time wow animate__animated animate__fadeIn animate__slower">{{ item.TIME }}
                    </p>
                    <p class="history_time wow animate__animated animate__fadeIn animate__slower">{{
                    item.DESCRIPTION }}
                    </p>


                    <div class="history_pic wow animate__animated animate__fadeIn animate__slower" v-if="item.PICTURE">
                        <img :src="item.PICTURE" alt="" class=" ">
                    </div>

                </div>


            </div>


            <!-- <img src="@/assets/img/about_history.svg" alt="">-->


        </div>

    </div>
</template>
