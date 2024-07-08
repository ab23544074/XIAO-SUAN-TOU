import HelloWorld from '@/components/HelloWorld.vue'
import { createRouter, createWebHistory } from 'vue-router'
//import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [

    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path:"/",
      redirect:"/home"
          
      
    },

    {
      path: '/home',
      name: 'home',
      component: () => import('../views/home.vue')
    },

    {
      path: '/Menu',
      name: 'Menu',
      
      component: () => import('../views/MenuView.vue')
    }
   
  ]
})

export default router
