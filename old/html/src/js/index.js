document.addEventListener('DOMContentLoaded', function() {
    const navContainer = document.querySelector('#nav');
    const navLinks = document.querySelectorAll('.nav-link, .subnav a');
    const groups = document.querySelectorAll('.group');

    // 初始化时仅显示第一个 .group，并激活第一个导航链接
    groups.forEach(group => group.classList.remove('active'));
    groups[0].classList.add('active');
    navLinks[0].classList.add('active');
    navLinks[0].setAttribute('aria-current', 'true');

    // 添加事件委托到导航栏
    navContainer.addEventListener('click', function(e) {
        const link = e.target.closest('.nav-link, .subnav a');
        if (link) {
            e.preventDefault();

            // 移除所有导航链接的激活状态
            navLinks.forEach(lnk => {
                lnk.classList.remove('active');
                lnk.setAttribute('aria-current', 'false');
            });
            link.classList.add('active');
            link.setAttribute('aria-current', 'true');

            // 隐藏所有 .group 元素
            groups.forEach(group => group.classList.remove('active'));

            // 显示目标按钮组
            const target = document.querySelector(link.getAttribute('data-target'));
            if (target) {
                target.classList.add('active');
            }
        }
    });
});
