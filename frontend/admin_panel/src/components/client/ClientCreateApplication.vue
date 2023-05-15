<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left">Оформить заказ</div>
        <v-btn  variant="outlined" class="mx-10" :to="{name: 'ClientBasket', params: {id_p: this.$route.params.id_p, cat_id: this.$route.params.cat_id}}">
            <v-icon icon="mdi-arrow-collapse-left" color="deep-orange" class="mr-2"></v-icon>назад
        </v-btn>
        <div class="text-h4 py-6 mx-10 text-left">Информация для доставки:</div>
        <v-row class="mx-10">
            <v-col  
                cols="12"
                md="3"
            >
                <v-text-field label="Город, населенный пункт" variant="underlined"></v-text-field>
            </v-col>
            <v-col  
                cols="12"
                md="3"
            >
                <v-text-field label="Улица" variant="underlined"></v-text-field>
            </v-col>
            <v-col  
                cols="12"
                md="3"
            >
                <v-text-field label="Дом" variant="underlined"></v-text-field>
            </v-col>
            <v-col  
                cols="12"
                md="3"
            >
                <v-text-field label="Корпус" variant="underlined"></v-text-field>
            </v-col>
        </v-row>

        <v-row class="mx-14 mt-5">
            <v-btn block  color="green-accent-4" :to="{name: 'ClientCreateApplication'}">
                Оформить заказ
            </v-btn>
        </v-row>
    </v-container>
</template>

<script>

</script>