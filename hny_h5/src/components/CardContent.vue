<template>
    <div class="flex flex-col w-fit h-fit items-center gap-4">
        <div class="w-[21.5rem] h-[36.875rem] items-center justify-center bg-[url('@/assets/img/container.png')] 
                bg-red-500rounded-md bg-no-repeat bg-cover bg-center flex flex-col py-10 px-8 gap-4">
            <div class="w-[12.5rem] h-12 bg-cover bg-no-repeat bg-center
                flex items-center justify-center gap-4 bg-[url('@/assets/img/title.png')]">
                <span class="text-[rgb(178,29,38)] text-lg font-[1000] text_shadow_red">测试中 测试 测试中</span>
            </div>
            <div class="w-full h-fit flex gap-2.5 items-center px-2">
                <div class="vertical_text tracking-[0.25rem] text-[#F7CE5A] font-[1000] 
                text-base text_shadow_yellow">测试内容</div>
                <div class="vertical_text tracking-[0.25rem] text-[#F7CE5A] font-[1000] 
                text-base text_shadow_yellow">测试内容第一句</div>
                <div class="vertical_text tracking-[0.25rem] text-[#F7CE5A] font-[1000] 
                text-base text_shadow_yellow">测试内容第二句</div>
                <div class="vertical_text tracking-[0.25rem] text-[#F7CE5A] font-[1000] 
                text-base text_shadow_yellow">测试内容第三句</div>
                <div class="vertical_text tracking-[0.25rem] text-[#F7CE5A] font-[1000] 
                text-base text_shadow_yellow">测试内容第四句</div>
                <div class="w-auto flex-grow h-40 bg-orange-500 ml-1"></div>
            </div>
            <div class="w-full h-0.25 bg-[#F7BA1E] px-4"></div>
            <div class="w-full h-auto flex flex-col gap-2 px-1">
                <div class="w-[4.25rem] h-[1.75rem] flex items-center justify-center
                bg-no-repeat bg-cover bg-center bg-[url('@/assets/img/subtitle.png')]">
                    <span class="text-[rgb(178,29,38)] text-sm font-[1000] text_shadow_red">测试</span>
                </div>
                <div class="w-full h-fit text-left px-2">
                    <span class="text-[#F7BA1E] text-sm font-[1000] text_shadow_yellow">
                        测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，
                    </span>
                </div>
                <div class="w-[4.25rem] h-[1.75rem] flex items-center justify-center
                bg-no-repeat bg-cover bg-center bg-[url('@/assets/img/subtitle.png')]">
                    <span class="text-[rgb(178,29,38)] text-sm font-[1000] text_shadow_red">测试</span>
                </div>
                <div class="w-full h-fit text-left px-2">
                    <span class="text-[#F7BA1E] text-sm font-[1000] text_shadow_yellow">
                    测试内容，测试内容，测试内容，测试内容，测试内容，测试内容</span>
                </div>
            </div>
        </div>

        <div class="flex w-full h-fit justify-between gap-4 px-4">
            <div class="w-[9.75rem] h-[4rem] bg-[url('@/assets/img/btn.png')] bg-cover bg-no-repeat bg-center">
                <span class="text-[rgb(178,29,38)] font-[1000] text-base block mt-2.5
                tracking-[0.1rem] text_shadow_white">测试按钮</span>
            </div>
            <div class="w-[9.75rem] h-[4rem] bg-[url('@/assets/img/btn.png')] bg-cover bg-no-repeat bg-center" @click.stop="test_close">
                <span class="text-[rgb(178,29,38)] font-[1000] text-base block mt-2.5
                tracking-[0.1rem] text_shadow_white">测试按钮</span>
            </div>
        </div>
    </div>
</template>

<style scoped>
.vertical_text {
    writing-mode: vertical-rl;
}
.text_shadow_yellow {
    text-shadow: 0px 2px 4px rgba(0, 0, 0, 0.25);
}
.text_shadow_red {
    text-shadow: 0px 0px 2px rgba(178, 29, 38, 0.25);
}
.text_shadow_white {
    text-shadow: 0px 0px 2px rgba(0, 0, 0, 0.10);
}
</style>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'CardContent',
    setup() {
        
    },
    methods: {
        test_close() {
            this.$emit(
                'getCloseStatu',
                {
                    'close': true
                }
            )
        }
    }
})
</script>