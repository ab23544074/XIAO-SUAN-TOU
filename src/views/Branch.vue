<script setup lang="ts">
import 'animate.css';
import "@/assets/css/branch.scss";

import 'bootstrap/dist/css/bootstrap.min.css';
import {onMounted, ref} from 'vue';
import 'animate.css';
import $ from 'jquery';



let histroy:any = [{
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
<style lang="scss">

</style>
<template>

    <div class="second container-fluid row m-0 p-0">



        <div class="col-lg-12 history">

            <h1 class="wow animate__animated animate__fadeIn">我們的朋友</h1>


            <div class="arrow"></div>


            <div class="history_text">

                <!--1-->

                <div v-for="item in histroy" :key="item" class="history_group">


                    <p class="history_time wow animate__animated animate__fadeIn animate__slower">{{ item.TIME }}</p>
                    <p class="history_time wow animate__animated animate__fadeIn animate__slower">{{ item.DESCRIPTION }}
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
