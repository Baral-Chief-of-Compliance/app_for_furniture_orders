// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "home" */ '@/views/Home.vue'),
      },
      {
        path: 'operator/categories',
        name: 'add_category',
        component: () => import('@/components/categories/Categories.vue')
      },
      {
        path: 'operator/categories/:id',
        name: 'category',
        component: () => import('@/components/categories/Categorie.vue')
      }
    ],
  },
  {
    path: '/login-employer',
    name: 'LoginEmployer',
    component: () => import('@/views/login/LoginEmp.vue')
  },
  {
    path: '/login-client',
    name: 'LoginClient',
    component: () => import('@/views/login/LoginCli.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
