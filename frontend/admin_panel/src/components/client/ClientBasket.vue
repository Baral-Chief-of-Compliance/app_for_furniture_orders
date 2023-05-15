<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left"> Корзина</div>
        <div class="text-h4 py-6 mx-10 text-left"> Сумма: <b> 6590 руб </b></div>

        <div class="text-h5 py-6 mx-10 text-left">Товары:</div>
        <v-card
                class="my-2 pa-6 mx-14 d-flex flex-row" 
                variant="outlined" 
            >
                <b class="pr-2">Название:</b> Стул деревянный Калатея
                <v-spacer></v-spacer>
                <b class="pr-2">Поставщик:</b> ООО 'Стройбат'
                <v-spacer></v-spacer>
                <b class="pr-2">Количество:</b>  <v-icon color="deep-orange" icon="mdi-minus"></v-icon> 1  <v-icon color="deep-orange" icon="mdi-plus"></v-icon> 
                <v-spacer></v-spacer>
                <b class="pr-2">Цена:</b>6590 <b class="pl-2">руб.</b>
        </v-card>
        <v-row class="mx-14 mt-15">
            <v-btn block  color="green-accent-4" :to="{name: 'ClientCreateApplication'}">
                Указать информацию для доставки
            </v-btn>
        </v-row>
    </v-container>
</template>

<script>
// export default{
//     methods: {
//         EnterClientCreateApplication(){
//             this.$router.push('/create_application')
//         }
//     }
// }
</script>