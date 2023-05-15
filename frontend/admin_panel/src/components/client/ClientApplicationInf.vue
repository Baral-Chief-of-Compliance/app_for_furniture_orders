<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left">Ифнормация о заказе</div>
        <div class="text-h5 py-6 mx-10 text-left">Товары:</div>
        <v-card
                class="my-2 pa-6 mx-14 d-flex flex-row" 
                variant="outlined" 
            >
                <b class="pr-2">Название:</b> Стул деревянный Калатея
                <v-spacer></v-spacer>
                <b class="pr-2">Поставщик:</b> ООО 'Стройбат'
                <v-spacer></v-spacer>
                <b class="pr-2">Количество:</b>  1 
                <v-spacer></v-spacer>
                <b class="pr-2">Цена:</b>6590 <b class="pl-2">руб.</b>
        </v-card>
        <div class="text-h5 py-6 mx-10 text-left">Адрес доставки:</div>
        <v-card
                class="my-2 pa-6 mx-14 d-flex flex-row" 
                variant="outlined" 
            >
                <b class="pr-2">Город, населенный пункт:</b> пгт Никель
                <v-spacer></v-spacer>
                <b class="pr-2">Улица:</b> улица Бредовая
                <v-spacer></v-spacer>
                <b class="pr-2">Дом:</b> 12 
        </v-card>
        <div class="text-h5 py-6 mx-10 text-left">Карта:</div>

        <div class="map ml-15">
                    <yandex-map
                        :coords="[69.405001, 30.202195]"
                        :zoom="4"
                    >
                        <ymap-marker 
                            :coords="[69.405001, 30.202195]" 
                            marker-id="1" 
                            :icon="{ color: 'red' }"
                        />

                        <ymap-marker 
                            :coords="[59.932036, 30.369866]" 
                            marker-id="2" 
                        />
                    </yandex-map>
        </div>

        <div class="text-h5 py-6 mx-10 text-left">Легенла карты:</div>
        <v-card class="my-2 pa-6 mx-14 d-flex flex-row">
            <v-icon color="red" icon="mdi-map-marker"></v-icon> <sapn class="pr-6">- пункт назначения доставки</sapn> <v-icon color="blue" icon="mdi-map-marker"></v-icon> - пункт отправки заказа
        </v-card>
    </v-container>
</template>

<script>

</script>

<style scoped>
.ymap-container {
    width: 1600px;
    height: 600px;
}

</style>