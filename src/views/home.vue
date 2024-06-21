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
        let screen_width:number = $(window).width();
        
        
        if (screen_width>1600) {
            return 4
        }else if (1000<screen_width && screen_width<1600){
            return 3

        }else if(screen_width < 1000){
            return 2
        }

        
        
        
    }

    const perview = ref(checkperview_count());

    $(document).ready(function(){
        console.log("start");
        
        
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

            <img src="../assets/img/home_pic.png" alt="" class="home_first_picture">

            
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
            <swiper-slide><img src="../assets/img/鹹酥雞.png" alt=""></swiper-slide>
                                    
            <swiper-slide><img src="../assets/img/丸子類.png" alt=""></swiper-slide> 
            <swiper-slide><img src="../assets/img/蔬菜.png" alt=""></swiper-slide>
            <swiper-slide><img src="../assets/img/雞皮.png" alt=""></swiper-slide>
            <swiper-slide><img src="../assets/img/魷魚絲.png" alt=""></swiper-slide>
            <swiper-slide><img src="../assets/img/雞蛋豆腐.png" alt=""></swiper-slide>
            <swiper-slide><img src="../assets/img/丸子類.png" alt=""></swiper-slide>
            <swiper-slide><img src="../assets/img/串串.png" alt=""></swiper-slide>
            <swiper-slide><img src="../assets/img/地瓜.png" alt=""></swiper-slide>
            <swiper-slide><img src="../assets/img/鹹酥雞.png" alt=""></swiper-slide>
            <swiper-slide><img src="../assets/img/丸子類.png" alt=""></swiper-slide> 
            <swiper-slide><img src="../assets/img/蔬菜.png" alt=""></swiper-slide>
            <swiper-slide><img src="../assets/img/雞皮.png" alt=""></swiper-slide>
            <swiper-slide><img src="../assets/img/魷魚絲.png" alt=""></swiper-slide>
        </swiper>
    </div>
    <div class="container">
        <div class="introducions row">
            <div class="col-lg-5">
                <img src="../assets/img/home_family_picture.png" alt="">
            </div>
            <div class="col-lg-7">
                <h2> 台南30年老店</h2>

                <p> 小蒜頭開立於民國82年<br>

                    獨特的胡椒和魷魚絲<br>
                    成為許多台南人心中的家鄉味<br>
                </p>
                <div class="home_about_link">

                    <a href="./about">關於小蒜頭</a>
                </div>
                

            </div>


        </div>

    </div>

</template>