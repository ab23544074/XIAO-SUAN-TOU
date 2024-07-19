<script setup lang="ts">

    
    import {Swiper, SwiperSlide} from 'swiper/vue';
    import 'bootstrap/dist/css/bootstrap.min.css';
    // import Swiper and modules styles
    import 'swiper/css';
    import 'swiper/css/navigation';
    import 'swiper/css/pagination';
    import {ref} from 'vue';
    import { Autoplay} from "swiper/modules";
    import $ from 'jquery';
    
    const modules = [Autoplay]
    
    

    const checkperview_count = () =>{
        let screen_width:any = $(window).width();
        
        
        if (screen_width>1600) {
            return 8
        }else if (1200<screen_width && screen_width<1600){
            return 5

        }else if (700<screen_width && screen_width<1000){
            return 4

        }else if (500<screen_width && screen_width<700){
            return 3

        }else if(screen_width < 500){
            return 2
        }
  
    }

    const perview = ref(checkperview_count());

    $(document).ready(function(){
        
        perview.value = checkperview_count()
        
    })
    
    window.onresize = () => {

        //reset perview
        perview.value = checkperview_count()
        
    }
    
</script>

<style scoped lang="scss">
    @import "@/assets/css/home.scss";
    
</style>
<template>
    
    
    <div class="first_picture container-fluid">
        
        
        <div>
            <img src="@/assets/img/home_png2.png" alt="" class="home_first_picture">
        </div>


        
           
        
        <div class="first_naming">

            <p class="font_1">
            歡迎光臨
            </p>

            <p class="font_2">

                小蒜頭
            </p>

            <p class="font_3">

                鹹酥雞
            </p>
        </div>
        
        
        
        
    </div>




    <div class="home_about">

        <h1> 創業故事 </h1>


        <div class="about_1">
            <div>
                
                <img src="@\assets\img\about_story1.jpg" alt="">

                
            </div>

            <h3>夢想</h3>
            <p>讀書時期的創業夢想</p>


        </div>

        <div class="about_2">

            <div>
                
                <img src="@\assets\img\about_story2.jpg" alt="">

                
            </div>

            <h3>勇闖</h3>
            <p>創業初期，努力打拼</p>
        </div>

        <div class="about_3">
            <div>
                
                <img src="@\assets\img\about_1.png" alt="">

                
            </div>

            <h3>茁壯</h3>
            <p>成為許多歸仁人最愛的美食</p>
        </div>

        <div class="more_store">
            <a href="./about"><button>─ 更多故事 ─</button></a>
        </div>
        

    </div>


    <div class="home_foods">

        <p>熱門美食</p>
        <swiper
        :slides-per-view="perview"
        allowTouchMove: false
        space-between="0"
        :speed="3000"
        :modules="modules"
        loop: true
        
        
        :autoplay="{ delay: 0, disableOnInteraction: false }"
        >
            <swiper-slide><img src="@/assets/img/鹹酥雞.png" alt=""></swiper-slide>
                                    
            <swiper-slide><img src="@/assets/img/丸子類.png" alt=""></swiper-slide> 
            <swiper-slide><img src="@/assets/img/蔬菜.png" alt=""></swiper-slide>
            <swiper-slide><img src="@/assets/img/雞皮.png" alt=""></swiper-slide>
            <swiper-slide><img src="@/assets/img/魷魚絲.png" alt=""></swiper-slide>
            <swiper-slide><img src="@/assets/img/雞蛋豆腐.png" alt=""></swiper-slide>
            <swiper-slide><img src="@/assets/img/丸子類.png" alt=""></swiper-slide>
            <swiper-slide><img src="@/assets/img/串串.png" alt=""></swiper-slide>
            <swiper-slide><img src="@/assets/img/地瓜.png" alt=""></swiper-slide>
            <swiper-slide><img src="@/assets/img/鹹酥雞.png" alt=""></swiper-slide>
            <swiper-slide><img src="@/assets/img/丸子類.png" alt=""></swiper-slide> 
            <swiper-slide><img src="@/assets/img/蔬菜.png" alt=""></swiper-slide>
            <swiper-slide><img src="@/assets/img/雞皮.png" alt=""></swiper-slide>
            <swiper-slide><img src="@/assets/img/魷魚絲.png" alt=""></swiper-slide>
        </swiper>
    </div>
    <div class="container">
        <div class="introducions row">
            <div class="col-lg-12">
                <h1>聯繫我們</h1>
            </div>
            <div class="col-lg-5">
                <h4> 小蒜頭鹹酥雞</h4>

                <p> 一起來品嘗傳統鹹酥雞</p>
                <h4>地址</h4>
                <p> 台南市歸仁區中正南路(總店)</p>
                <h4>營業時間</h4>
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
                
                <div class="more_store">
                    <a href="./address"><button>─ 更多據點 ─</button></a>
                </div>
            </div>

            <div class="col-lg-7">
                <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d14694.339678250059!2d120.2942227!3d22.965509!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x346e71e603fd6cfb%3A0x6301298435e544f5!2z5bCP6JKc6aCt6bm96YWl6ZueKOatuOS7geW6lyk!5e0!3m2!1szh-TW!2stw!4v1721385290670!5m2!1szh-TW!2stw" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
        </div>

    </div>

</template>