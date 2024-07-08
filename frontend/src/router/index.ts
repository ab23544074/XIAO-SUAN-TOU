import { createRouter, createWebHistory } from 'vue-router'
//import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [

     /*{
      path: '/',
      name: 'vuehome',
      component: HomeView
     },*/
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },

    {
      path: '/home',
      name: 'home',
      component: () => import('../views/home.vue')
    },

    /*
    {
      path: '/about',
      name: 'about',
      
      component: () => import('../views/about.vue')
    },
    {
      path: '/Menu',
      name: 'Menu',
      
      component: () => import('../views/Menu.vue')
    }*/
   
  ]
})

export default router
